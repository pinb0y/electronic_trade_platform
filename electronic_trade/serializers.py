from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError

from electronic_trade.models import Supplier, Product, Contact


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'model',
            'release_date',
        ]


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'email',
            'country',
            'city',
            'street',
            'street_number',
        ]


class EditContactSerializer(ContactSerializer):
    id = serializers.IntegerField(
        required=False,
        write_only=False,
    )


class NestedSupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id',
            'name',
            'supplier_type',
        ]


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    supplier = NestedSupplierSerializer()
    supplier_type = serializers.CharField(source='get_supplier_type_display')

    class Meta:
        model = Supplier
        fields = (
            'id',
            'name',
            'supplier_type',
            'hierarchy',
            'supplier',
            'debt',
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'debt',
            'created_at',
            'updated_at',
        )


class DetailSupplierSerializer(SupplierSerializer):
    products = ProductSerializer(
        source='products.all',
        many=True,
        read_only=True,
    )

    contacts = ContactSerializer(
        source='contacts.all',
        many=True,
        read_only=False,
    )

    class Meta(SupplierSerializer.Meta):
        fields = SupplierSerializer.Meta.fields + (
            'products',
            'contacts',
        )


class EditSupplierSerializer(DetailSupplierSerializer):
    supplier = fields.IntegerField(
        required=False,
        allow_null=True,
    )

    products = fields.ListField(
        child=serializers.IntegerField(),
        required=False,
    )

    contacts = EditContactSerializer(
        many=True,
        required=False,
    )

    @staticmethod
    def __update_contacts(instance, validated_data):
        if "contacts" not in validated_data:
            return
        contacts = validated_data.pop("contacts")

        remove_items = {item.id: item for item in instance.contacts.all()}
        for item in contacts:
            item_id = item.get("id", None)
            if item_id is None:
                instance.contacts.create(**item)
            elif remove_items.get(item_id, None) is not None:
                instance_item = remove_items.pop(item_id)
                Contact.objects.filter(id=instance_item.id).update(**item)
        for item in remove_items.values():
            item.delete()

    @staticmethod
    def __update_supplier(instance, validated_data):
        if "supplier" not in validated_data:
            return
        supplier_id = validated_data.pop("supplier")

        if supplier_id is None:
            instance.supplier = None
            return

        if supplier_id == instance.id:
            raise ValidationError(
                detail={
                    "supplier": "Сan not appoint self as a supplier",
                },
            )

        supplier = Supplier.objects.filter(pk=supplier_id)
        if not supplier:
            raise ValidationError(
                detail={
                    "supplier": f"Supplier with id {supplier_id} not found",
                },
            )

        instance.supplier = supplier.first()
        return

    def update(self, instance, validated_data):
        self.__update_contacts(instance, validated_data)
        self.__update_supplier(instance, validated_data)

        for field in validated_data:
            setattr(
                instance,
                field,
                validated_data.get(field, getattr(instance, field)),
            )
        instance.save()
        return instance
