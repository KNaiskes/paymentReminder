from django import forms

DAYS_CHOICES = (
    ('', '-----'),
    ('seven', '7 Days'),
    ('thirty', '30 Days'),
    ('sixty', '60 Days'),
    ('ninety', '90 days'),
)

class DateHistorySearchForm(forms.Form):
    days = forms.ChoiceField(label='days', help_text="Select days: ",choices = DAYS_CHOICES)

    def get_selected_option(self):
        import datetime
        data = self.cleaned_data['days']
        range_options = { 'seven': 7,'thirty': 30, 'sixty': 60, 'ninety': 90 }

        try:
            selected_option = range_options[data]
        except(KeyError):
            selected_option = datetime.date.today()

        return selected_option
