class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }
}

class Department {
    Employee employee;

    Department(Employee employee) {
        this.employee = employee;
    }
}

public class Main {
    public static void main(String[] args) {
        Employee employee = new Employee("Alice");

        Department department = new Department(employee);

        System.out.println(department.employee.name);
    }
}