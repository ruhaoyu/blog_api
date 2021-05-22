"""test

Revision ID: 743eddd2abee
Revises: 6a2237c91843
Create Date: 2021-05-20 00:02:54.309925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '743eddd2abee'
down_revision = '6a2237c91843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('test', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'test')
    # ### end Alembic commands ###