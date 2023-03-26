"""Initial migration

Revision ID: 8dc5bc70ff25
Revises: b6c4dfce0b8f
Create Date: 2023-03-23 21:53:49.749467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dc5bc70ff25'
down_revision = 'b6c4dfce0b8f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.Integer(), nullable=True),
    sa.Column('OsId', sa.Integer(), nullable=True),
    sa.Column('date_only', sa.Date(), nullable=True),
    sa.Column('time_only', sa.Time(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('rrhhid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_appointments_id'), 'appointments', ['id'], unique=False)
    op.create_table('confirmations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('date_only', sa.Date(), nullable=True),
    sa.Column('time_only', sa.Time(), nullable=True),
    sa.Column('persCelular', sa.BigInteger(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_confirmations_id'), 'confirmations', ['id'], unique=False)
    op.create_table('patient_contact_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.Integer(), nullable=True),
    sa.Column('persCelular', sa.BigInteger(), nullable=True),
    sa.Column('persmail', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patient_contact_info_id'), 'patient_contact_info', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_patient_contact_info_id'), table_name='patient_contact_info')
    op.drop_table('patient_contact_info')
    op.drop_index(op.f('ix_confirmations_id'), table_name='confirmations')
    op.drop_table('confirmations')
    op.drop_index(op.f('ix_appointments_id'), table_name='appointments')
    op.drop_table('appointments')
    # ### end Alembic commands ###