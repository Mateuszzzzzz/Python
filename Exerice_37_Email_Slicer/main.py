def check_if_mail(em):
        if '@' not in em:
            print('That is not valid email!')
        else:
            answer=[]
            for elements in em:
                if elements!='@':
                    answer.append(elements)
                else:
                    break

            answer2=''.join(answer)
            answer_rest=em.replace(answer2, '').replace('@', '')
            print(f"First part of the email: {answer2}")
            print(f"Rest of the email address is: {answer_rest}")


if __name__ == '__main__':
    em = str(input('Please input email: '))
    check_if_mail(em)

