from currency.models import Rate, Source

from django import forms


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type',
            'buy',
            'sale',
            'source',
        )


class SourceForm(forms.ModelForm):  # 名前は慣例的にこう書く。文字数制限などのルールはモデルに書く
    class Meta:
        model = Source  # テーブル名
        fields = (
            'name',
            'source_url',
            'logo',
        )
