import os
import shutil


def remove_local_data():
    shutil.rmtree(os.path.join('{{ cookiecutter.repo_name }}', 'data'))


def create_shared_folder():
    os.mkdir("{{ cookiecutter.shared_project_path }}")
    os.mkdir(os.path.join("{{ cookiecutter.shared_project_path }}", 'data'))

    to_add = ['raw', 'interim', 'processed']
    for name in to_add:
        os.mkdir(
            os.path.join(
                "{{ cookiecutter.shared_project_path }}", 'data', name))


def main():
    if '{{ cookiecutter.shared_project }}':
        remove_local_data()
        create_shared_folder()


if __name__ == "__main__":
    main()
