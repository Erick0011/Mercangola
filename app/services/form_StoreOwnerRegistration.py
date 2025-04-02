from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, URL


class StoreOwnerRegistrationForm(FlaskForm):
    # Campos do usuário (User)
    name = StringField("Nome", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    telefone = StringField("Telefone", validators=[Optional(), Length(min=9, max=20)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])

    # Campos da loja (Store)
    store_name = StringField("Nome da Loja", validators=[DataRequired(), Length(min=2, max=255)])
    slug = StringField("Slug (URL única da loja)", validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField("Descrição da Loja", validators=[Optional(), Length(max=500)])

    # Contato da loja
    phone = StringField("Telefone da Loja", validators=[Optional(), Length(min=9, max=20)])
    email_store = StringField("Email da Loja", validators=[Optional(), Email()])
    website = StringField("Website", validators=[Optional(), URL()])

    # Endereço da loja
    address = StringField("Endereço", validators=[Optional(), Length(max=255)])
    city = StringField("Cidade", validators=[Optional(), Length(max=100)])
    state = StringField("Estado", validators=[Optional(), Length(max=100)])
    country = StringField("País", validators=[Optional(), Length(max=100)])
    latitude = FloatField("Latitude", validators=[Optional()])
    longitude = FloatField("Longitude", validators=[Optional()])

    # Redes sociais
    facebook = StringField("Facebook", validators=[Optional(), URL()])
    instagram = StringField("Instagram", validators=[Optional(), URL()])
    twitter = StringField("Twitter", validators=[Optional(), URL()])



    submit = SubmitField("Registrar Loja")
