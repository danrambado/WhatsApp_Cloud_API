"""create_form_table

Revision ID: 2ab94804f9d0
Revises: 7aeff1f60fc9
Create Date: 2023-03-26 18:12:53.870322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ab94804f9d0'
down_revision = '7aeff1f60fc9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forms_send',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('idpersona', sa.Integer(), nullable=True),
    sa.Column('persCelular', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forms_send_id'), 'forms_send', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_forms_send_id'), table_name='forms_send')
    op.drop_table('forms_send')
    # ### end Alembic commands ###