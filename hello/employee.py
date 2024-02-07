from dataclasses import dataclass, field
import datetime

@dataclass(frozen=True)
class Employee:
    name: str
    hire_date: datetime.date
    salary: float = field(repr=False)  # Example of using field() for additional options, such as disabling display when print
    
    # Instance method
    def years_of_service(self) -> int:
        """Calculate years of service."""
        return datetime.date.today().year - self.hire_date.year
    
    @classmethod
    def from_name_and_years(cls, name: str, years: int):
        """Factory method to create an Employee instance from name and years of service."""
        hire_date = datetime.date.today() - datetime.timedelta(days=365 * years)
        return cls(name=name, hire_date=hire_date, salary=100000.50)
    
    @staticmethod
    def is_full_time(hours_worked: int) -> bool:
        """Determine if a given number of hours qualifies as full-time employment."""
        return hours_worked >= 40
    