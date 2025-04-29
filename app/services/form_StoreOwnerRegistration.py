from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class StoreOwnerRegistrationForm(FlaskForm):
    # Usuário
    name = StringField("Nome", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])

    # Loja
    store_name = StringField("Nome da Loja", validators=[DataRequired(), Length(min=2, max=255)])
    slug = StringField("Slug da Loja (URL única)", validators=[DataRequired(), Length(min=2, max=100)])

    submit = SubmitField("Criar Loja")
