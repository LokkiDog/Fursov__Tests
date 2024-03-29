# Generated by Django 4.0.6 on 2022-09-22 10:05

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('date_follow', models.DateTimeField(blank=True, null=True)),
                ('date_expire', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('token_v3', models.TextField(blank=True, default=None, null=True, unique=True, verbose_name='WildV3Token')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ABCBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=7, null=True), blank=True, null=True, size=4)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=4)),
            ],
        ),
        migrations.CreateModel(
            name='LiquidityBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=64, null=True), blank=True, null=True, size=6)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, default=None, null=True), blank=True, null=True, size=6)),
            ],
        ),
        migrations.CreateModel(
            name='ProfitabilityBaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=127, null=True, verbose_name='Артикул'), blank=True, null=True, size=24)),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Прибыль на 1 шт'), blank=True, null=True, size=24)),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('google_title', models.CharField(blank=True, default=None, max_length=127, null=True, unique=True)),
                ('slug', models.CharField(blank=True, default=None, max_length=64, null=True, unique=True)),
                ('has_detail', models.BooleanField(default=False)),
                ('secondary', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'sheet',
                'verbose_name_plural': 'sheets',
            },
        ),
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spreadsheet_id', models.CharField(max_length=127)),
                ('spreadsheet_title', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'spreadsheet',
                'verbose_name_plural': 'spreadsheets',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'tariff',
                'verbose_name_plural': 'tariffs',
            },
        ),
        migrations.CreateModel(
            name='ABCConclusion',
            fields=[
                ('abcbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.abcbasemodel')),
            ],
            bases=('configurator.abcbasemodel',),
        ),
        migrations.CreateModel(
            name='ABCDays',
            fields=[
                ('abcbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.abcbasemodel')),
            ],
            bases=('configurator.abcbasemodel',),
        ),
        migrations.CreateModel(
            name='ABCRent',
            fields=[
                ('abcbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.abcbasemodel')),
            ],
            bases=('configurator.abcbasemodel',),
        ),
        migrations.CreateModel(
            name='LiquidRemains',
            fields=[
                ('liquiditybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.liquiditybasemodel')),
            ],
            bases=('configurator.liquiditybasemodel',),
        ),
        migrations.CreateModel(
            name='LiquidRent',
            fields=[
                ('liquiditybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.liquiditybasemodel')),
            ],
            bases=('configurator.liquiditybasemodel',),
        ),
        migrations.CreateModel(
            name='RentDays',
            fields=[
                ('liquiditybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.liquiditybasemodel')),
            ],
            bases=('configurator.liquiditybasemodel',),
        ),
        migrations.CreateModel(
            name='RentRemains',
            fields=[
                ('liquiditybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.liquiditybasemodel')),
            ],
            bases=('configurator.liquiditybasemodel',),
        ),
        migrations.CreateModel(
            name='TopProfitProfitability',
            fields=[
                ('profitabilitybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.profitabilitybasemodel')),
            ],
            bases=('configurator.profitabilitybasemodel',),
        ),
        migrations.CreateModel(
            name='WorstProfitProfitability',
            fields=[
                ('profitabilitybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='configurator.profitabilitybasemodel')),
            ],
            bases=('configurator.profitabilitybasemodel',),
        ),
        migrations.CreateModel(
            name='WeeklyReportSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_count', models.IntegerField(blank=True, default=None, null=True, verbose_name='Выкуп, штуки')),
                ('percent_fact', models.IntegerField(blank=True, default=None, null=True, verbose_name='Сделано')),
                ('sheet_title', models.ForeignKey(default='week', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyReportOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_count', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки')),
                ('percent_fact', models.IntegerField(blank=True, default=None, null=True, verbose_name='Сделано')),
                ('sheet_title', models.ForeignKey(default='week', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyReportGoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realize', models.IntegerField(blank=True, default=None, null=True, verbose_name='К перечислению')),
                ('orders_rub', models.FloatField(blank=True, default=None, null=True, verbose_name='Заказы, рубли')),
                ('logistic', models.FloatField(blank=True, default=None, null=True, verbose_name='Выкуп, рубли')),
                ('sold', models.FloatField(blank=True, default=None, null=True, verbose_name='Логистика, рубли')),
                ('sheet_title', models.ForeignKey(default='week', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyReportDynamicOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Дата'), blank=True, null=True, size=6)),
                ('orders_data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки'), blank=True, null=True, size=6)),
                ('sold_data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Продажи, штуки'), blank=True, null=True, size=6)),
                ('sheet_title', models.ForeignKey(default='week', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_id', models.CharField(max_length=64)),
                ('update_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('favourite', models.BooleanField(default=False)),
                ('sheet_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet')),
                ('spreadsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.spreadsheet')),
            ],
            options={
                'verbose_name': 'user_sheet',
                'verbose_name_plural': 'user_sheets',
            },
        ),
        migrations.CreateModel(
            name='UserCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wb_token', models.CharField(blank=True, default=True, max_length=127, null=True)),
                ('name', models.CharField(blank=True, default=True, max_length=127, null=True)),
                ('organization', models.CharField(blank=True, default=True, max_length=127, null=True)),
                ('token', models.CharField(blank=True, default=True, max_length=255, null=True)),
                ('x64key', models.CharField(blank=True, default=True, max_length=64, null=True)),
                ('supplier_id', models.CharField(blank=True, default=True, max_length=127, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopWorstCategoriesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=127, null=True, verbose_name='Категория')),
                ('orders_rub', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, рубли')),
                ('sheet_title', models.ForeignKey(default='orders-categories', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopOrdersTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Артикул')),
                ('nomenclature', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Номенклатура')),
                ('orders_amount', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки')),
                ('orders_rub', models.FloatField(blank=True, default=None, null=True, verbose_name='Заказы, рубли')),
                ('sheet_title', models.ForeignKey(default='dynamic-art-count', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopOrdersGraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Артикул')),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки'), blank=True, null=True, size=7)),
                ('sheet_title', models.ForeignKey(default='dynamic-art-count', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopCategoriesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=127, null=True, verbose_name='Категория')),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, рубли.'), blank=True, null=True, size=6)),
                ('sheet_title', models.ForeignKey(default='orders-categories', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopCategoriesDonut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Категория'), blank=True, null=True, size=6)),
                ('orders_rub', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, рубли.'), blank=True, null=True, size=6)),
                ('sheet_title', models.ForeignKey(default='orders-categories', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopBrandsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, default=None, max_length=127, null=True, verbose_name='Бренд')),
                ('orders_amount', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки')),
                ('sheet_title', models.ForeignKey(default='dynamic-art-count', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sheet',
            name='tariff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='configurator.tariff'),
        ),
        migrations.CreateModel(
            name='SelfSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_id', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Номенклатура')),
                ('article', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Артикул')),
                ('total_amount', models.IntegerField(blank=True, default=None, null=True, verbose_name='Выкупы, шт')),
                ('total_sum', models.SmallIntegerField(blank=True, default=None, null=True, verbose_name='Выкупы, рубли')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profitabilitybasemodel',
            name='sheet_title',
            field=models.ForeignKey(default='profitability', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug'),
        ),
        migrations.AddField(
            model_name='profitabilitybasemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MonthlyReportSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_count', models.IntegerField(blank=True, default=None, null=True, verbose_name='Выкуп, штуки')),
                ('percent_fact', models.IntegerField(blank=True, default=None, null=True, verbose_name='Сделано')),
                ('sheet_title', models.ForeignKey(default='month', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReportOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_count', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки')),
                ('percent_fact', models.IntegerField(blank=True, default=None, null=True, verbose_name='Сделано')),
                ('sheet_title', models.ForeignKey(default='month', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReportGoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realize', models.IntegerField(blank=True, default=None, null=True, verbose_name='К перечислению')),
                ('orders_rub', models.FloatField(blank=True, default=None, null=True, verbose_name='Заказы, рубли')),
                ('logistic', models.FloatField(blank=True, default=None, null=True, verbose_name='Выкуп, рубли')),
                ('sold', models.FloatField(blank=True, default=None, null=True, verbose_name='Логистика, рубли')),
                ('sheet_title', models.ForeignKey(default='month', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReportDynamicOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Дата'), blank=True, null=True, size=6)),
                ('orders_data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки'), blank=True, null=True, size=6)),
                ('sold_data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Продажи, штуки'), blank=True, null=True, size=6)),
                ('sheet_title', models.ForeignKey(default='month', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='liquiditybasemodel',
            name='sheet_title',
            field=models.ForeignKey(default='liquidity', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug'),
        ),
        migrations.AddField(
            model_name='liquiditybasemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DynamicOrdersWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='Дата')),
                ('data', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказано, рубли')),
                ('sheet_title', models.ForeignKey(default='day', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesBaseStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall', models.IntegerField(blank=True, default=None, null=True, verbose_name='Итого')),
                ('overall_last_day', models.IntegerField(blank=True, default=None, null=True, verbose_name='Итого за последний день')),
                ('count', models.IntegerField(blank=True, default=None, null=True, verbose_name='Количество категорий')),
                ('sheet_title', models.ForeignKey(default='orders-categories', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BaseStatProfitability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.IntegerField(blank=True, default=None, null=True, verbose_name='Операционная прибыль')),
                ('average_profit', models.IntegerField(blank=True, default=None, null=True, verbose_name='Средняя прибыль за 1 шт')),
                ('prime_cost', models.IntegerField(blank=True, default=None, null=True, verbose_name='Себестоимость')),
                ('logistics', models.IntegerField(blank=True, default=None, null=True, verbose_name='Логистика')),
                ('storage', models.IntegerField(blank=True, default=None, null=True, verbose_name='Хранение')),
                ('sheet_title', models.ForeignKey(default='profitability', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BaseStatisticCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_amount', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказы, штуки')),
                ('increase_amount', models.IntegerField(blank=True, default=None, null=True, verbose_name='Прирост/убыток заказов в количестве')),
                ('orders_rub', models.FloatField(blank=True, default=None, null=True, verbose_name='Заказы, рубли')),
                ('increase_rub', models.IntegerField(blank=True, default=None, null=True, verbose_name='Прирост/убыток заказов в рублях')),
                ('orders_sells', models.IntegerField(blank=True, default=None, null=True, verbose_name='Продажи, рубли')),
                ('increase_sells', models.IntegerField(blank=True, default=None, null=True, verbose_name='Прирост/убыток продаж')),
                ('sheet_title', models.ForeignKey(default='day', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BaseStatDynamicOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_count', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказано, штуки')),
                ('orders_rub', models.IntegerField(blank=True, default=None, null=True, verbose_name='Заказано, рубли')),
                ('orders_rows', models.IntegerField(blank=True, default=None, null=True, verbose_name='Товаров')),
                ('orders_zero', models.IntegerField(blank=True, default=None, null=True, verbose_name='Товар без заказов')),
                ('sheet_title', models.ForeignKey(default='dynamic-art-count', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='abcbasemodel',
            name='sheet_title',
            field=models.ForeignKey(default='abc', on_delete=django.db.models.deletion.CASCADE, to='configurator.sheet', to_field='slug'),
        ),
        migrations.AddField(
            model_name='abcbasemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='tariff',
            field=models.ForeignKey(blank=True, default='Оптимальный', null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurator.tariff', to_field='title'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
