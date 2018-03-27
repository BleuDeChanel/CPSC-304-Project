from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClubMemberships(models.Model):
    membershipid = models.IntegerField(primary_key=True)
    tier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'club_memberships'


class CustomerRegisterPrivate(models.Model):
    privatetitle = models.CharField(unique=True, max_length=20)
    phonenumber = models.ForeignKey('Customers', models.DO_NOTHING, db_column='phonenumber')
    name = models.CharField(max_length=50)
    privateregnumber = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'customer_register_private'


class CustomerRegisterProgram(models.Model):
    phonenumber = models.ForeignKey('Customers', models.DO_NOTHING, db_column='phonenumber')
    name = models.CharField(max_length=12)
    programtitle = models.CharField(max_length=20)
    programregnumber = models.IntegerField(primary_key=True)
    officesin = models.ForeignKey('OfficeEmployees', models.DO_NOTHING, db_column='officesin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_register_program'


class CustomerReservesCourt(models.Model):
    phonenumber = models.ForeignKey('Customers', models.DO_NOTHING, db_column='phonenumber')
    name = models.CharField(max_length=50) # this should be fk too
    courtnumber = models.IntegerField(primary_key=True)
    date = models.DateField()
    starttime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    officesin = models.ForeignKey('OfficeEmployees', models.DO_NOTHING, db_column='officesin')

    class Meta:
        managed = False
        db_table = 'customer_reserves_court'
        unique_together = (('courtnumber', 'date', 'starttime'),)


class Customers(models.Model):
    phonenumber = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    membershipid = models.ForeignKey(ClubMemberships, models.DO_NOTHING, db_column='membershipid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'
        unique_together = (('phonenumber', 'name'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Instructors(models.Model):
    inssin = models.CharField(primary_key=True, max_length=9)
    phonenumber = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructors'


class MembershipPlans(models.Model):
    tier = models.IntegerField(primary_key=True)
    fee = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership_plans'


class OfficeEmployees(models.Model):
    officesin = models.CharField(primary_key=True, max_length=9)
    phonenumber = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_employees'


class PrivateCourseCourtReservation(models.Model):
    privatetitle = models.CharField(max_length=20)
    courtnumber = models.IntegerField(primary_key=True)
    date = models.DateField()
    starttime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True) 
    officesin = models.ForeignKey(OfficeEmployees, models.DO_NOTHING, db_column='officesin')

    class Meta:
        managed = False
        db_table = 'private_course_court_reservation'
        unique_together = (('courtnumber', 'date', 'starttime'),)


class PrivateTaught(models.Model):
    privatetitle = models.CharField(primary_key=True, max_length=20)
    private_fee = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    inssin = models.ForeignKey(Instructors, models.DO_NOTHING, db_column='inssin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'private_taught'


class ProgramCourtReservation(models.Model):
    courtnumber = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    starttime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    officesin = models.ForeignKey(OfficeEmployees, models.DO_NOTHING, db_column='officesin')
    programtitle = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'program_court_reservation'
        unique_together = (('courtnumber', 'date', 'starttime'),)


class ProgramTaught(models.Model):
    programtitle = models.CharField(primary_key=True, max_length=20)
    numberofpeople = models.IntegerField(blank=True, null=True)
    fee = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    inssin = models.ForeignKey(Instructors, models.DO_NOTHING, db_column='inssin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_taught'


class StudentMembers(models.Model):
    membershipid = models.ForeignKey(ClubMemberships, models.DO_NOTHING, db_column='membershipid', primary_key=True)
    sid = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'student_members'
