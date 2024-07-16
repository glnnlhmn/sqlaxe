import argparse
import sqlglot
from sqlglot import Dialect, Expression, exp


class SQLFormatter:
    def __init__(self, dialect='mysql', output_dialect='mysql', **kwargs):

        self.pretty_print = kwargs['pretty_print'] or True
        self.dialect = dialect
        self.output_dialect = output_dialect or self.dialect

    def get_statements(self, expressions):

        pretty_printed_statements = []
        for expressions in expressions:
            if expressions is None:
                continue
            if expressions == "":
                continue

            append_semicolon = True

            if isinstance(expressions, exp.Semicolon):
                append_semicolon = False

            if self.output_dialect != self.dialect:
                pretty_printed_statement = write.generate(
                    expressions, copy=False, pretty=self.pretty_print, identify=True
                )
            else:
                pretty_printed_statement = expressions.sql(pretty=self.pretty_print, identify=True)

            if append_semicolon:
                pretty_printed_statement = pretty_printed_statement + ";"

            pretty_printed_statements.append(pretty_printed_statement)

        return pretty_printed_statements

    def format(self, sql_content):
        return "\n\n".join(self.get_statements(sql_content))