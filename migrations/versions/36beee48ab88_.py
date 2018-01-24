"""empty message

Revision ID: 36beee48ab88
Revises: 564ccb24a657
Create Date: 2018-01-24 21:20:23.781169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36beee48ab88'
down_revision = '564ccb24a657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author_id', sa.String(length=100), nullable=False))
    op.create_foreign_key(None, 'post', 'front_user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'author_id')
    # ### end Alembic commands ###
