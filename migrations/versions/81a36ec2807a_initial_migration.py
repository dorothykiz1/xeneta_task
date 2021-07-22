"""Initial migration.

Revision ID: 81a36ec2807a
Revises: 
Create Date: 2021-07-21 22:49:36.110708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81a36ec2807a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ports',
    sa.Column('code', sa.Text(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('parent_slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('prices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orig_code', sa.String(), nullable=True),
    sa.Column('dest_code', sa.String(), nullable=True),
    sa.Column('day', sa.Date(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('regions',
    sa.Column('slug', sa.Text(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('parent_slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('regions')
    op.drop_table('prices')
    op.drop_table('ports')
    # ### end Alembic commands ###
