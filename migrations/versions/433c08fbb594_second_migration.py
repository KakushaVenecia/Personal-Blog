"""Second Migration

Revision ID: 433c08fbb594
Revises: 
Create Date: 2022-05-16 03:13:19.789627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '433c08fbb594'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'admins', 'users', ['user_id'], ['id'])
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.alter_column('blogs', 'admin_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.alter_column('blogs', 'admin_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('blogs', 'user_id')
    op.drop_constraint(None, 'admins', type_='foreignkey')
    op.drop_column('admins', 'user_id')
    # ### end Alembic commands ###
