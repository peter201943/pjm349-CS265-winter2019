FILE_NAME=$(basename $(FILE))


#TARGETS
.PHONY: test clean generate_clean generate_headers build run

run: build generate_headers generate_clean
	./scripts/pad_clean_ics.sh $(notdir $(FILE)).temp
	./scripts/generate_table.sh $(notdir $(FILE)).temp.pad

build: ./scripts/clean_ics.sh ./scripts/generate_table.awk ./scripts/generate_table.sh \
		./scripts/get_table_headers.awk ./scripts/get_table_headers.sh ./scripts/pad_empty_fields.awk \
		./scripts/pad_empty_fields.sh ./icalconv.sh ./scripts/pad_clean_ics.sh ./test.sh
	chmod +x ./scripts/*.awk
	chmod +x ./scripts/*.sh
	chmod +x ./icalconv.sh
	chmod +x ./test.sh

generate_headers: generate_clean ./scripts/get_table_headers.awk ./scripts/get_table_headers.sh
	./scripts/get_table_headers.sh $(notdir $(FILE)).temp

generate_clean: ./scripts/clean_ics.sh $(FILE)
ifndef FILE
	$(error FILE is not set. Try make <target> FILE=<file_name>)
endif
	./scripts/clean_ics.sh $(FILE)

test: build ./icalconv.sh
	./icalconv.sh test/ICS_TEST_11.ics
	mv out.html test/ICS_TEST_11.html
	./icalconv.sh test/ICS_TEST_12.ics
	mv out.html test/ICS_TEST_12.html
	./icalconv.sh test/ICS_TEST_13.ics
	mv out.html test/ICS_TEST_13.html
	./icalconv.sh test/ideal.ics
	mv out.html test/ideal_test.html
	./icalconv.sh test/VAlarm.ics
	mv out.html test/VAlarm_test.html
	./test.sh
	make clean-non-test

clean:
	rm -f temp_out *.ics.temp headers *.html *.ics *.ics.*
	rm -f test/ICS_TEST_*.html
	rm -f test/*_test.html

clean-non-test:
	rm -f temp_out *.ics.temp headers *.html *.ics *.ics.*
