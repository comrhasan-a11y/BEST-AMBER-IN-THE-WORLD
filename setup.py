from setuptools import setup, find_packages

setup(
    name='best-amber-in-the-world',
    version='0.1.0',
    description='Advanced ICT/Smart Money Concepts trading system with backtesting, DXY correlation, session awareness, confluence scoring, and news filtering.',
    author='comrhasan-a11y',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'smartmoneyconcepts>=0.0.26',
        'backtrader>=1.9.76',
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'plotly>=5.0.0',
        'python-forex>=1.0',
        'yfinance>=0.1.70',
    ],
    python_requires='>=3.8',
)