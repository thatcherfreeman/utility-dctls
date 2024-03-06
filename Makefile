lint:
	clang-format -i Effects/*.dctl
	clang-format -i Operations/*.dctl
	clang-format -i Utilities/*.dctl

all: lint