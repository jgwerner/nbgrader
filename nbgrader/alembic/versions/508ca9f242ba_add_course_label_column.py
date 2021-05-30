"""add course_label column

Revision ID: 508ca9f242ba
Revises: e43177bfe90b
Create Date: 2021-05-29 22:34:51.135666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '508ca9f242ba'
down_revision = 'e43177bfe90b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('course', sa.Column('course_label', sa.String))


def downgrade():
    op.drop_column('course', 'course_label')
