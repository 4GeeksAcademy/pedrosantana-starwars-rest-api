"""empty message

Revision ID: 577efc4c7463
Revises: 85e891dd9d7a
Create Date: 2023-08-16 06:17:02.943935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '577efc4c7463'
down_revision = '85e891dd9d7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint('favorites_people_id_key', type_='unique')
        batch_op.drop_constraint('favorites_planet_id_key', type_='unique')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint('people_name_key', type_='unique')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_constraint('planets_name_key', type_='unique')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.create_unique_constraint('planets_name_key', ['name'])

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.create_unique_constraint('people_name_key', ['name'])

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.create_unique_constraint('favorites_planet_id_key', ['planet_id'])
        batch_op.create_unique_constraint('favorites_people_id_key', ['people_id'])

    # ### end Alembic commands ###
