# hCaptcha Solver

This project is an advanced hCaptcha solver utilizing the `tls_client` library for managing sessions and threading for handling concurrent tasks. It also integrates a replier module to provide responses for captcha tasks. This README will guide you through the setup and usage of the solver.

## Features

- **Session Management:** Uses `tls_client` for creating secure sessions.
- **Multithreading:** Utilizes `ThreadPoolExecutor` for handling multiple captcha tasks simultaneously.
- **Captcha Interaction:** Retrieves and submits captcha challenges.
- **Custom Headers and Proxies:** Allows custom headers and proxy configurations.
- **Enhanced Motion Data:** Integrates motion data for captcha solving.

## Setup

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or later
- Required Python packages

### Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Basic Usage

0. **Start the server `hsw_api.py`.**

1. **Import the Necessary Modules:**

    ```python
    from solver import Solver
    ```

2. **Initialize the Solver:**

    ```python
    sitekey = "your_site_key"
    host = "your_host"
    proxy = "your_proxy"  # Optional
    rqdata = "your_rqdata"  # Optional

    solver = Solver(sitekey, host, proxy, rqdata)
    ```

3. **Solve the Captcha:**

    ```python
    result = solver.solve()
    print(f"Solved Captcha UUID: {result}")
    ```

### Advanced Configuration

- **Session Headers:**
  
  Customize headers within the `Solver` class if needed.

- **Proxy Settings:**

  Set up proxies by providing the proxy URL when initializing the `Solver`.

### Example Script

Here's an example script to demonstrate the usage:

```python
from solver import Solver

# Configuration
sitekey = "your_site_key"
host = "your_host"
proxy = "your_proxy"  # Optional
rqdata = "your_rqdata"  # Optional

# Initialize Solver
solver = Solver(sitekey, host, proxy, rqdata)

# Solve Captcha
result = solver.solve()

# Output Result
print(f"Solved Captcha: {result}")
```

## Acknowledgements

This project is an improved and fixed version of an existing repository. Special thanks to the original authors for their groundwork. (https://github.com/fCaptcha/hCaptcha-Solver).

## Troubleshooting

- **Common Issues**
    - Ensure all dependencies are installed.
    - Verify the proxy configuration if used.
    - Check the site key and host for accuracy.

- **Logs and Debugging**:
    - The script includes print statements for logging and debugging purposes. Review these logs to trace issues.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are greatly appreciated.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

