from django.db import models


class Pitching(models.Model):
    season = models.IntegerField(db_column='Season')
    team = models.CharField(db_column='Team', max_length=12)
    w = models.IntegerField(db_column='W')
    l = models.IntegerField(db_column='L')
    era = models.DecimalField(db_column='ERA', max_digits=12, decimal_places=2)
    g = models.IntegerField(db_column='G')
    gs = models.IntegerField(db_column='GS')
    cg = models.IntegerField(db_column='CG')
    sho = models.IntegerField(db_column='ShO')
    sv = models.IntegerField(db_column='SV')
    ip = models.DecimalField(db_column='IP', max_digits=12, decimal_places=2)
    tbf = models.IntegerField(db_column='TBF')
    h = models.IntegerField(db_column='H')
    r = models.IntegerField(db_column='R')
    er = models.IntegerField(db_column='ER')
    hr = models.IntegerField(db_column='HR')
    bb = models.IntegerField(db_column='BB')
    ibb = models.IntegerField(db_column='IBB')
    hbp = models.IntegerField(db_column='HBP')
    wp = models.IntegerField(db_column='WP')
    so = models.IntegerField(db_column='SO')
    avg = models.DecimalField(db_column='AVG', max_digits=65, decimal_places=30)
    whip = models.DecimalField(db_column='WHIP', max_digits=12, decimal_places=2)
    babip = models.DecimalField(db_column='BABIP', max_digits=65, decimal_places=30)
    lob = models.DecimalField(db_column='LOB', max_digits=65, decimal_places=30)
    fip = models.DecimalField(db_column='FIP', max_digits=12, decimal_places=2)
    rar = models.DecimalField(db_column='RAR', max_digits=12, decimal_places=2)
    war = models.DecimalField(db_column='WAR', max_digits=12, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'pitching'


class Fielding(models.Model):
    season = models.IntegerField(db_column='Season')
    team = models.CharField(db_column='Team', max_length=12)
    inn = models.IntegerField(db_column='Inn')
    po = models.IntegerField(db_column='PO')
    a = models.IntegerField(db_column='A')
    e = models.IntegerField(db_column='E')
    dp = models.IntegerField(db_column='DP')
    sb = models.IntegerField(db_column='SB')
    cs = models.IntegerField(db_column='CS')
    pb = models.IntegerField(db_column='PB')
    wp = models.IntegerField(db_column='WP')
    fp = models.DecimalField(db_column='FP', max_digits=65, decimal_places=30)

    class Meta:
        managed = True
        db_table = 'fielding'


class Batting(models.Model):
    season = models.IntegerField(db_column='Season')
    team = models.CharField(db_column='Team', max_length=12)
    g = models.IntegerField(db_column='G')
    ab = models.IntegerField(db_column='AB')
    pa = models.IntegerField(db_column='PA')
    h = models.IntegerField(db_column='H')
    singles = models.IntegerField(db_column='1B')
    doubles = models.IntegerField(db_column='2B')
    triples = models.IntegerField(db_column='3B')
    hr = models.IntegerField(db_column='HR')
    r = models.IntegerField(db_column='R')
    rbi = models.IntegerField(db_column='RBI')
    bb = models.IntegerField(db_column='BB')
    ibb = models.IntegerField(db_column='IBB')
    so = models.IntegerField(db_column='SO')
    hbp = models.IntegerField(db_column='HBP')
    sf = models.IntegerField(db_column='SF')
    sh = models.IntegerField(db_column='SH')
    gdp = models.IntegerField(db_column='GDP')
    sb = models.IntegerField(db_column='SB')
    cs = models.IntegerField(db_column='CS')
    avg = models.DecimalField(db_column='AVG', max_digits=65, decimal_places=30)
    obp = models.DecimalField(db_column='OBP', max_digits=65, decimal_places=30)
    slg = models.DecimalField(db_column='SLG', max_digits=65, decimal_places=30)
    ops = models.DecimalField(db_column='OPS', max_digits=65, decimal_places=30)
    iso = models.DecimalField(db_column='ISO', max_digits=65, decimal_places=30)
    babip = models.DecimalField(db_column='BABIP', max_digits=65, decimal_places=30)
    woba = models.DecimalField(db_column='wOBA', max_digits=65, decimal_places=30)
    wraa = models.DecimalField(db_column='wRAA', max_digits=12, decimal_places=2)
    wrc = models.IntegerField(db_column='wRC')
    rar = models.DecimalField(db_column='RAR', max_digits=12, decimal_places=2)
    waroff = models.DecimalField(db_column='WARoff', max_digits=12, decimal_places=2)
    wrc_field = models.IntegerField(db_column='wRC+')
    wsb = models.DecimalField(db_column='wSB', max_digits=12, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'batting'