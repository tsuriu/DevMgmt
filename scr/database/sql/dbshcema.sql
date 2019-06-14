create database argo_devices;

use argo_devices;

create table hosts (
  host_id interger primary key autoincrement,
  host name varchar(40) not null,
  host_type int(1) unsigned not null,
  host_ip int(4) unsigned not null, /* INET_ATON("127.0.0.1") examples to INSERT and SELECT value. */
  host_snmp interger,
  host_vendor varchar(255) not null,
  host_model varchar(255) not null,
  constraint fk_HstSnmp foreign key (host_snmp) references snmp_profile (_id)
);

create table olt (
  olt_id interger primary key autoincrement,
  host_id int unsigned not null,
  mgmt_cnt int unsigner not null,
  pon_cnt int unsigner not null,
  onu_auth_cnt int unsigner not null,
  onu_unauth_cnt int unsigner not null
);  

create table olt_card ();

create table olt_pon  ();

create table olt_onu  ():

