from django.test import TestCase

from dummy.models import testform
from dummy.serializers import FormSerializer


class FormModelAndSerializerTests(TestCase):
    def test_serializer_accepts_valid_data(self):
        payload = {
            'name': 'Alice',
            'phone': 123456789,
            'email': 'alice@example.com',
            'password': 'super-secret',
        }

        serializer = FormSerializer(data=payload)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        instance = serializer.save()
        self.assertEqual(instance.name, 'Alice')
        self.assertEqual(instance.email, 'alice@example.com')
        self.assertEqual(instance.password, 'super-secret')

    def test_model_can_be_created(self):
        form = testform.objects.create(
            name='Bob',
            phone=987654321,
            email='bob@example.com',
            password='another-secret',
        )

        self.assertEqual(testform.objects.count(), 1)
        self.assertEqual(form.password, 'another-secret')
