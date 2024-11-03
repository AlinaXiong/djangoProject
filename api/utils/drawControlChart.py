import matplotlib.pyplot as plt


def calculate_control_limits(base_times, factor):
    """Calculate upper and lower control limits based on basic response time"""
    return [t * (1 + factor) for t in base_times], [t * (1 - factor) for t in base_times]


def plot_component_times(components, times, label, marker=None, linestyle='-', color='black'):
    """Draw component response timeline diagram"""
    plt.plot(components, times, marker=marker, linestyle=linestyle, label=label, color=color)


def main():
    # Component list
    components = [
        "Frontend UI", "Load Balancer", "API Gateway",
        "Middleware", "Auth Service", "Database",
        "Caching", "Message Queue", "Network", "Logging"
    ]

    # Response time data
    bob_times = [0.15, 0.10, 0.20, 0.25, 0.10, 0.30, 0.15, 0.10, 0.10, 0.05]
    wow_times = [0.30, 0.25, 0.50, 0.80, 0.40, 0.70, 0.60, 0.20, 0.20, 0.15]

    # Calculate control limits
    control_factor = 0.5
    cl_upper, cl_lower = calculate_control_limits(bob_times, control_factor)

    # Set up chart
    plt.figure(figsize=(12, 6))

    plot_component_times(components, bob_times, label='BOB Times', marker='o')
    plot_component_times(components, wow_times, label='WOW Times', marker='x')
    plot_component_times(components, cl_upper, label='Upper Control Limit', linestyle='--', color='red')
    plot_component_times(components, cl_lower, label='Lower Control Limit', linestyle='--', color='blue')

    # Set chart properties
    plt.title('Component Response Time Control Chart')
    plt.xlabel('Module')
    plt.ylabel('Response Time (seconds)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Show chart
    plt.show()


# Make sure the main function is only run when the script is executed directly
if __name__ == "__main__":
    main()
