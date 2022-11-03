def main():
    movie_len_min = int(input("Enter movie length (minutes): "))
    print(f"Movie length: {movie_len_min // 60} hour(s), {movie_len_min % 60} minute(s)")
    return 1


if __name__ == '__main__':
    main()