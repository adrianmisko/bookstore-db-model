"""add cascade constraint

Revision ID: b33c554c8cb2
Revises: 008db9234c45
Create Date: 2019-01-03 11:35:04.758202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b33c554c8cb2'
down_revision = '008db9234c45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('taggings_tag_fkey', 'taggings', type_='foreignkey')
    op.drop_constraint('taggings_book_id_fkey', 'taggings', type_='foreignkey')
    op.create_foreign_key(None, 'taggings', 'book', ['book_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'taggings', 'tag', ['tag'], ['tag'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'taggings', type_='foreignkey')
    op.drop_constraint(None, 'taggings', type_='foreignkey')
    op.create_foreign_key('taggings_book_id_fkey', 'taggings', 'book', ['book_id'], ['id'])
    op.create_foreign_key('taggings_tag_fkey', 'taggings', 'tag', ['tag'], ['tag'])
    # ### end Alembic commands ###