from VkAPI import VkAPI


def main():
    id1 = 5
    id2 = 1212121
    q = VkAPI.my_frieds_get_mutual(id1, id2)
    VkAPI.user_info_by_id(q)

if __name__ == '__main__':
    main()
