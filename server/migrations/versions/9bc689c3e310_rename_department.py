"""rename department

Revision ID: 9bc689c3e310
Revises: 2a939c1ba9a6
Create Date: 2024-05-01 16:46:29.565074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bc689c3e310'
down_revision = '2a939c1ba9a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
