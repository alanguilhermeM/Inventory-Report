from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory


class SimpleReport(Report):
    def __init__(self) -> None:
        self.estoques = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.estoques.append(inventory)

    def generate(self) -> str:
        oldest = None
        expiration = None
        largest_inventory_company = None

        # for estoque in self.estoques:
        #     if not oldest or oldest > estoque.get_earliest_date():
        #         oldest = estoque.get_earliest_date()
        #     if not expiration or expiration > estoque.get_latest_date():
        #         expiration = estoque.get_latest_date()
        #     if (
        #         not largest_inventory_company
        #         or largest_inventory_company[1] < estoque.count_total()
        #     ):
        #         largest_inventory_company = (estoque.get_company(), estoque.count_total())

        # return (
        #     f"Oldest manufacturing date: {oldest}\n"
        #     f"Closest expiration date: {expiration}\n"
        #     f"Company with the largest inventory: {largest_inventory_company[0]}"
        # )


