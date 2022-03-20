"""empty message

Revision ID: 051e386f2acd
Revises: 
Create Date: 2022-03-19 17:56:06.948718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051e386f2acd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('beds', sa.Integer(), nullable=True),
    sa.Column('baths', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Numeric(precision=14, scale=2), nullable=True),
    sa.Column('pic', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###
