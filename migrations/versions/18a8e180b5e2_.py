"""empty message

Revision ID: 18a8e180b5e2
Revises: 97f9a337d93a
Create Date: 2023-04-27 14:11:22.974410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18a8e180b5e2'
down_revision = '97f9a337d93a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=200), server_default='', nullable=False))
        batch_op.add_column(sa.Column('body', sa.Text(), server_default='', nullable=False))
        batch_op.add_column(sa.Column('dt_created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('dt_updated', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('dt_updated')
        batch_op.drop_column('dt_created')
        batch_op.drop_column('body')
        batch_op.drop_column('title')

    # ### end Alembic commands ###
