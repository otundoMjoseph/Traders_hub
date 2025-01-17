"""empty message

Revision ID: abe6256f4fff
Revises: e6d9920ccab7
Create Date: 2024-07-11 10:34:14.889216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abe6256f4fff'
down_revision = 'e6d9920ccab7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedbacks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))
        batch_op.drop_column('rating')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedbacks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.INTEGER(), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###
