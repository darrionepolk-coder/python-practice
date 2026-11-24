class Employee:
    """Store information about one employee."""

    # --- 1. Initializer --------------------------------------------
    def __init__(self, emp_id, name, department, job_title):
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department
        self.__job_title = job_title

    # --- 2. Accessor (getter) methods -------------------------------
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    # --- 3. Mutator (setter) methods --------------------------------
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    # --- 4. __str__ -------------------------------------------------
    def __str__(self):
        return (f"Employee ID: {self.__emp_id}\n"
                f"Name: {self.__name}\n"
                f"Department: {self.__department}\n"
                f"Job Title: {self.__job_title}")
