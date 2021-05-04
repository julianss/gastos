import peewee as pw
from flr import BaseModel, db

class CategoriaGasto(BaseModel):
    name = pw.CharField(verbose_name="Nombre")

CategoriaGasto.r()

class Gasto(BaseModel):
    name = pw.CharField(verbose_name="Concepto")
    fecha = pw.DateField(verbose_name="Fecha")
    categoria = pw.ForeignKeyField(CategoriaGasto, verbose_name="Categoría")
    monto = pw.FloatField(verbose_name="Monto")
    chat_id = pw.CharField(verbose_name="Telegram chat id")

    @classmethod
    def resumen(cls, chat_id, fecha):
        cr = db.execute_sql("""--begin-sql
            select c.name, sum(monto)
            from gasto g
            join categoria_gasto c on g.categoria_id=c.id
            where chat_id=%s and fecha::text like %s
            group by c.name
        --endsql
        """, (chat_id, fecha))
        return [row for row in cr.fetchall()]

Gasto.r()

class BotState(BaseModel):
    name = pw.CharField(verbose_name="Concepto")
    monto = pw.FloatField(verbose_name="Monto")
    chat_id = pw.CharField(verbose_name="Telegram chat id")

