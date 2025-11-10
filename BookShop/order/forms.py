from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Manipal', 'Manipal'),
		('Patna', 'Patna'),
		('Noida', 'Noida'),
		('Jhotwara', 'Jhotwara'),
	)

	DISCRICT_CHOICES = (
		('Udupi', 'Udupi'), 
		('Bihar', 'Bihar'),
		('Delhi', 'Delhi'),
		('Jaipur', 'Jaipur'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Paytm', 'Paytm'),
		('GooglePay','GooglePay'),
		('ApplePay','ApplePay')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES)

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
