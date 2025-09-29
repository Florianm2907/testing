#include <iostream>
#include <cmath>
#include <boost/multiprecision/cpp_dec_float.hpp>

using namespace boost::multiprecision;

int main() {
    cpp_dec_float_50 radius = 6374340;
    cpp_dec_float_50 distance = 87654321;
    cpp_dec_float_50 gravity_const = 6.67430E-11;

    cpp_dec_float_50 grav_force(cpp_dec_float_50 distance) {
        cpp_dec_float_50 M1 = (9.81 * (radius * radius) / gravity_const);
        cpp_dec_float_50 r = distance + radius;
        cpp_dec_float_50 g = gravity_const * (M1 / (r * r));
        return g;
    }

    cpp_dec_float_50 acceleration(cpp_dec_float_50 accel, cpp_dec_float_50 gravity) {
        cpp_dec_float_50 velocity = sqrt(accel * accel + 2 * gravity);
        return velocity;
    }

    cpp_dec_float_50 calculate_height(cpp_dec_float_50 time) {
        cpp_dec_float_50 current_acceleration = 0;
        cpp_dec_float_50 current_distance = 0;
        cpp_dec_float_50 current_time = 0;

        while (current_time < time) {
            current_acceleration = acceleration(current_acceleration, grav_force(radius + current_distance));
            cpp_dec_float_50 time_step = current_acceleration / grav_force(radius + current_distance);
            current_time += time_step;
            current_distance += 1;
        }

        return current_distance;
    }

    cpp_dec_float_50 given_time = 755367.5351298475669;
    cpp_dec_float_50 height = calculate_height(given_time);

    std::cout << "Das Objekt war " << height << " Meter über der Erde zur Zeit " << given_time << " Sekunden." << std::endl;

    return 0;
}
