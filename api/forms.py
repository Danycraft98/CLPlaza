from itertools import repeat

from django.forms import Form, ChoiceField, Select, CharField, TextInput, PasswordInput

REQUEST_LIST = [list(repeat('GET', 2)), list(repeat('POST', 2))]
AUTH_LIST = [list(repeat('No Auth', 2)), list(repeat('Basic Auth', 2)), list(repeat('OAuth', 2))]

LANG_LIST = [('KorService', '한국어/국문 서비스'), ('EngService', '영어 서비스'), ('RusService', '러시아어/노어 서비스')]
CAT_LIST = [('searchFestival', '행사 정보 조회'), ('categoryCode', '서비스 분류 코드 조회'), ('detailImage', '이미지정보 조회')]
NUM_ROW_LIST = [list(repeat(10, 2)), list(repeat(20, 2)), list(repeat(30, 2))]


class PostmanAPIForm(Form):
    request = ChoiceField(choices=REQUEST_LIST, widget=Select(attrs={
        'class': 'form-select col-2'
    }))
    url = CharField(label='URL', widget=TextInput(attrs={
        'class': 'form-control'
    }))

    auth = ChoiceField(choices=AUTH_LIST, widget=Select(attrs={
        'class': 'form-select col-2'
    }))
    username = CharField(required=False, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }))
    password = CharField(required=False, widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))

    key = CharField(required=False, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'key'
    }))
    value = CharField(required=False, widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'value'
    }))

    class Meta:
        fields = '__all__'
