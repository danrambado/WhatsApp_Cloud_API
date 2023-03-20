"""Revision

Revision ID: 01061db2d1ee
Revises: cd6dd8d18a25
Create Date: 2023-03-19 20:34:27.627681

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '01061db2d1ee'
down_revision = 'cd6dd8d18a25'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_appointments_id', table_name='appointments')
    op.drop_table('appointments')
    op.drop_index('ix_my_table_id', table_name='my_table')
    op.drop_table('my_table')
    op.drop_table('appoinments')
    op.drop_index('ix_person_id', table_name='person')
    op.drop_table('person')
    op.drop_index('ix_Appointments_id', table_name='Appointments')
    op.drop_table('Appointments')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Appointments',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Appointments_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('OsId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_only', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('time_only', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rrhhid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Appointments_pkey')
    )
    op.create_index('ix_Appointments_id', 'Appointments', ['id'], unique=False)
    op.create_table('person',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('OsId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_only', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('time_only', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rrhhid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='person_pkey')
    )
    op.create_index('ix_person_id', 'person', ['id'], unique=False)
    op.create_table('appoinments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('OsId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_only', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('time_only', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rrhhid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='appoinments_pkey')
    )
    op.create_table('my_table',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('OsId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_only', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('time_only', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rrhhid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='my_table_pkey')
    )
    op.create_index('ix_my_table_id', 'my_table', ['id'], unique=False)
    op.create_table('appointments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('OsId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_only', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('time_only', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rrhhid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='appointments_pkey')
    )
    op.create_index('ix_appointments_id', 'appointments', ['id'], unique=False)
    # ### end Alembic commands ###
