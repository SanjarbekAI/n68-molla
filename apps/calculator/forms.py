from django import forms

from apps.calculator.models import ResultModel


class CalculatorForm(forms.ModelForm):
    class Meta:
        model = ResultModel
        exclude = ['result', 'created_at']

    def save(self, commit=True):
        num1 = self.cleaned_data.get('num1')
        num2 = self.cleaned_data.get('num2')
        sign = self.cleaned_data.get('sign')

        # Handle all four operations
        if sign == "+":
            result = num1 + num2
        elif sign == "-":
            result = num1 - num2
        elif sign == "*":  # or "×" depending on your form value
            result = num1 * num2
        elif sign == "/":  # or "÷" depending on your form value
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        # Create the model instance
        instance = super().save(commit=False)
        instance.result = result

        if commit:
            instance.save()

        return instance
