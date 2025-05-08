from setuptools import setup, find_packages

setup(
    name="nova-ai-chatbot",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai",
        "speechrecognition",
        "pyttsx3",
        "pillow",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'nova = src.nova:main',
        ],
    },
    include_package_data=True,
    author="",
    description="NOVA is a futuristic AI chatbot with dynamic avatars, voice capabilities, multi-personality support, and OpenAI integration.",
    license="MIT",
)
