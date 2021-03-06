"""Add weekly metrics table

Revision ID: d760c7a84ba3
Revises: b466c9da106b
Create Date: 2019-02-22 09:26:28.129637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd760c7a84ba3'
down_revision = 'b466c9da106b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weekly_metrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comp_id', sa.Integer(), nullable=True),
    sa.Column('desktop_hits', sa.Integer(), nullable=True),
    sa.Column('mobile_hits', sa.Integer(), nullable=True),
    sa.Column('new_users_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comp_id'], ['competitions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('weekly_metrics', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_weekly_metrics_comp_id'), ['comp_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weekly_metrics', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_weekly_metrics_comp_id'))

    op.drop_table('weekly_metrics')
    # ### end Alembic commands ###
