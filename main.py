from modules.solver     import Solver
from concurrent.futures import ThreadPoolExecutor

def main():
    Solver(
        sitekey='4c672d35-0701-42b2-88c3-78380b0db560',
        host='discord.com'
    ).solve()

if __name__ == "__main__":
    main()