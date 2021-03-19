import peewee as pw
from flare import BaseModel

class CategoriaGasto(BaseModel):
    name = pw.CharField(verbose_name="Nombre")

CategoriaGasto.r()

class Gasto(BaseModel):
    name = pw.CharField(verbose_name="Concepto")
    fecha = pw.DateField(verbose_name="Fecha")
    categoria = pw.ForeignKeyField(CategoriaGasto, verbose_name="Categoría")
    monto = pw.FloatField(verbose_name="Monto")
    chat_id = pw.CharField(verbose_name="Telegram chat id")

Gasto.r()

class BotState(BaseModel):
    name = pw.CharField(verbose_name="Concepto")
    monto = pw.FloatField(verbose_name="Monto")
    chat_id = pw.CharField(verbose_name="Telegram chat id")

