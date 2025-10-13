from django import forms
from .models import Contact
from django import forms
from .models import Contact

class ContactUsForm(forms.ModelForm):
    # فیلدها را دستی تعریف می‌کنیم تا همیشه پیام سفارشی نمایش داده شود
    name = forms.CharField(
        required=True,
        label="نام شما",
        error_messages={'required': 'لطفاً نام خود را وارد کنید ❌'}
    )
    email = forms.EmailField(
        required=True,
        label="ایمیل شما",
        error_messages={
            'required': 'وارد کردن ایمیل الزامی است ❌',
            'invalid': 'آدرس ایمیل معتبر نیست ⚠️'
        }
    )
    subject = forms.CharField(
        required=True,
        label="موضوع پیام",
        error_messages={'required': 'موضوع را بنویسید ⚠️'}
    )
    message = forms.CharField(
        required=True,
        label="متن پیام",
        widget=forms.Textarea,
        error_messages={'required': 'بدون پیام نمی‌توان ارسال کرد!'}
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


# اول از این روش استفاده کردم ولی چون با مدل در تداخل بود و پیغام های خطای سفارشی توی textfildها درست نمایش داده نمیشد از روش بالا استفاده کردم 
# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#         labels = {
#             'name': 'نام شما',
#             'email': 'ایمیل شما',
#             'subject': 'موضوع پیام',
#             'message': 'متن پیام',
#         }
#         error_messages = {
#             'name': {'required': 'لطفاً نام خود را وارد کنید ❌'},
#             'email': {
#                 'required': 'وارد کردن ایمیل الزامی است ❌',
#                 'invalid': 'آدرس ایمیل معتبر نیست ⚠️',
#             },
#             'subject': {'required': 'موضوع را بنویسید ⚠️'},
#             'message': {'required': 'بدون پیام نمی‌توان ارسال کرد!'},
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # ✅ همه فیلدها را required کن
#         for field_name, field in self.fields.items():
#             field.required = True

#             # ✅ خطای فارسی عمومی اگر error_messages نداشت
#             if 'required' not in field.error_messages:
#                 field.error_messages['required'] = f'پر کردن فیلد {self.fields[field_name].label} الزامی است ❌'



   


  
    