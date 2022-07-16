# Запуск тестов из урока lesson_3_2_step13
import pytest
import os
import Module3.Lesson3_2.lesson_3_2_step13 as source

# get path for source
source_path = os.path.abspath(source.__file__)
# run tests from source
pytest.main([source_path])
