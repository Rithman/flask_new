"""empty message

Revision ID: e2e2c5472d23
Revises: 
Create Date: 2023-04-24 13:51:49.619429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2e2c5472d23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('is_staff', sa.Boolean(), nullable=False),
    sa.Column('email', sa.String(length=255), server_default='', nullable=False),
    sa.Column('_password', sa.LargeBinary(), nullable=True),
    sa.Column('first_name', sa.String(length=120), server_default='', nullable=True),
    sa.Column('last_name', sa.String(length=120), server_default='', nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
