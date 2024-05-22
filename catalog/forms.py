from django.forms import ModelForm, forms
from catalog.models import Product, Version
from django.db.models import BooleanField


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        exclude = ('views_counter',)

    def clean_name(self):

        clean_data = self.cleaned_data.get('name')
        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        if clean_data.lower() in forbidden_words:
            raise forms.ValidationError(f'Наименование не должно содержать слова: {forbidden_words}')
        else:
            return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data.get('description')
        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        if clean_data.lower() in forbidden_words:
            raise forms.ValidationError(f'Описание не должно содержать слова: {forbidden_words}')
        else:
            return clean_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        exclude = ("is_active_version",)
