import lesson_2_1_step5 as main_step


def get_x(web_driver):
    return int(web_driver.find_element_by_id("treasure").get_attribute("valuex"))


if __name__ == "__main__":
    page = "http://suninjuly.github.io/get_attribute.html"
    # пройди квест ;-)
    # решение выполнено в шаге 5, кроме функции get_x
    main_step.complete_form(page, get_x)
