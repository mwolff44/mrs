# Generated by Django 2.0 on 2017-12-28 19:06

from django.conf import settings
from django.db import migrations, models


'''
http://paste.debian.net/1002158/
'''

TRIGGER = '''
create table mrsrequest_formid (date date, seq int);
insert into mrsrequest_formid values ('1900-01-01', 0);
create or replace function mrsrequest_formid_seq_increment() returns text as $$
  update mrsrequest_formid set
    date = current_date,
    seq = case when date <= current_date then seq + 1 else 0 end
  returning to_char(date, 'YYYYMMDD') || LPAD(seq::text, 4, '0');
$$ language sql;
CREATE OR REPLACE FUNCTION mrsrequest_formid_pre_insert()
RETURNS trigger
AS $$
    BEGIN
        SELECT mrsrequest_formid_seq_increment() INTO NEW.form_id;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER mrsrequest_formid_trigger
BEFORE INSERT ON mrsrequest_mrsrequest
FOR EACH ROW EXECUTE PROCEDURE mrsrequest_formid_pre_insert();
'''


class Migration(migrations.Migration):

    dependencies = [
        ('mrsrequest', '0001_initial'),
    ]

    operations = [
    ]

    if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql':
        operations.append(migrations.RunSQL(TRIGGER))
